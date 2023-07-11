from flask import Flask
from flask_restplus import Api, Resource

from linestar.plc_magnet_mover import PLCMagnetMover


app = Flask(__name__)
api = Api(app, title='Linestar PLC Magnet Mover', description='API endpoints for PLC Magnet Mover')


@api.route('/wake')
class Wake(Resource):
    def post(self):
        client = PLCMagnetMover()
        client.connect()
        client.wake()
        client.close()
        return {'message': 'System woke up successfully'}, 200


@api.route('/move_to_home')
class MoveToHome(Resource):
    def post(self):
        client = PLCMagnetMover()
        client.connect()
        client.move_to_home()
        client.close()
        return {'message': 'Moved to home position successfully'}, 200


@api.route('/go_to_position/<float:x>/<float:y>')
class GoToPosition(Resource):
    def post(self, x, y):
        client = PLCMagnetMover()
        client.connect()
        client.go_to_position(x, y)
        client.close()
        return {'message': f'Moved to position ({x}, {y}) successfully'}, 200


@api.route('/report_location')
class ReportLocation(Resource):
    def get(self):
        client = PLCMagnetMover()
        client.connect()
        location = client.report_location()
        client.close()
        return {'location': location}, 200


@api.route('/report_error_margin')
class ReportErrorMargin(Resource):
    def get(self):
        client = PLCMagnetMover()
        client.connect()
        error_margin = client.report_error_margin()
        client.close()
        return {'error_margin': error_margin}, 200


if __name__ == '__main__':
    app.run(debug=True)

