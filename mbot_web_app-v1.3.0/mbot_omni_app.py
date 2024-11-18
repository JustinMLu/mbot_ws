from app import app, socket, lcm_manager, connection_manager

EMIT_PERIOD = 0.1
HANDLE_PERIOD = 1e-3


def run_lcm():
    while True:
        lcm_manager.handleOnce()
        socket.sleep(HANDLE_PERIOD)  # Not sure if needed.


def emit_msgs():
    while True:
        if connection_manager.connected:
            lcm_manager.emit_msgs()
        socket.sleep(EMIT_PERIOD)


if __name__ == '__main__':
    # Start the LCM handler and message emitter. Note these threads should not block.
    socket.start_background_task(run_lcm)
    socket.start_background_task(emit_msgs)
    # Start the Flask app.
    socket.run(app, host="0.0.0.0", port=5000)
