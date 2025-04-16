use serde::{Deserialize, Serialize};
use std::sync::{Arc, Mutex};
use std::thread;
use tauri::Emitter;
use tiny_http::{Header, Method, Request, Response, Server};

#[derive(Serialize, Deserialize, Clone)]
pub struct Status {
    pub in_meeting: bool,
    pub drone_on: bool,
    pub video_on: bool,
}

pub fn start_http_server(state: Arc<Mutex<Status>>, app_handle: tauri::AppHandle) {
    thread::spawn(move || {
        let server = Server::http("0.0.0.0:5000").expect("Failed to start server");

        for request in server.incoming_requests() {
            handle_request(request, &state, &app_handle);
        }
    });
}

fn with_cors<R: std::io::Read + Send + 'static>(mut response: Response<R>) -> Response<R> {
    response.add_header(Header::from_bytes("Access-Control-Allow-Origin", "*").unwrap());
    response
}

fn handle_request(mut request: Request, state: &Arc<Mutex<Status>>, app_handle: &tauri::AppHandle) {
    match (request.method(), request.url()) {
        (&Method::Get, "/status") => {
            let status = state.lock().unwrap();
            let body = serde_json::to_string(&*status).unwrap();

            let response = Response::from_string(body)
                .with_header(Header::from_bytes("Content-Type", "application/json").unwrap());

            let _ = request.respond(with_cors(response));
        }

        (&Method::Post, "/status") => {
            let mut content = String::new();
            if let Err(_) = request.as_reader().read_to_string(&mut content) {
                let response = Response::from_string("Invalid request").with_status_code(400);
                let _ = request.respond(with_cors(response));
                return;
            }

            match serde_json::from_str::<Status>(&content) {
                Ok(new_status) => {
                    let mut status = state.lock().unwrap();
                    *status = new_status.clone();
                    let _ = app_handle.emit("status_changed", new_status.clone());

                    let response = Response::from_string("Updated");
                    let _ = request.respond(with_cors(response));
                }
                Err(_) => {
                    let response = Response::from_string("Invalid JSON").with_status_code(400);
                    let _ = request.respond(with_cors(response));
                }
            }
        }

        _ => {
            let response = Response::from_string("Not Found").with_status_code(404);
            let _ = request.respond(with_cors(response));
        }
    }
}
