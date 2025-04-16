// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
mod http_server;

use http_server::{start_http_server, Status};
use std::sync::{Arc, Mutex};
use tauri::Emitter;

fn main() {
    tauri::Builder::default()
        .setup(|app| {
            let status = Arc::new(Mutex::new(Status {
                in_meeting: false,
                drone_on: false,
                video_on: false,
            }));

            // Emit default state to frontend immediately
            let _ = app.emit("status_changed", status.lock().unwrap().clone());

            // Start HTTP server and pass state
            start_http_server(status.clone(), app.handle().clone());

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri app");
}
