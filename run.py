import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
    debug_mode = app.config.get('DEBUG', False)
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    print(f" * Starting Flask server on http://{host}:{port}/ (Debug: {debug_mode})")
    app.run(host=host, port=port, debug=debug_mode, use_reloader=debug_mode, threaded=True)
