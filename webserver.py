from flask import Flask
from flask_restx import Api, Resource

from plc_magnet_mover import PLCMagnetMover

app = Flask(__name__)
api = Api(app, default_endpoint='https://linestarautomation.com/api/v0.0.4', version='0.0.4', title='Linestar Machine Controller APIs', description='Machine Controller API endpoints for Linestar Automation Developer Platform' )

ns = api.namespace('controllers/magnet-mover', description='PLC Magnet Mover API')

@ns.route('/connect/<string:ip>')
class Connect(Resource):
    @ns.doc('connect')
    def get(self, ip):
        """Connect to the PLC"""
        magnet_mover = PLCMagnetMover(ip)
        magnet_mover.connect()
        return {'message': 'Connected to PLC'}

@ns.route('/wake')
class Wake(Resource):
    @ns.doc('wake')
    def get(self):
        """Wake up the system"""
        magnet_mover = PLCMagnetMover()
        magnet_mover.wake()
        return {'message': 'System woke up successfully'}

@ns.route('/move_to_home')
class MoveToHome(Resource):
    @ns.doc('move_to_home')
    def get(self):
        """Move to the home position"""
        magnet_mover = PLCMagnetMover()
        magnet_mover.move_to_home()
        return {'message': 'Moved to home position successfully'}

@ns.route('/go_to_position/<float:x>/<float:y>')
class GoToPosition(Resource):
    @ns.doc('go_to_position')
    def get(self, x, y):
        """Go to a specific position"""
        magnet_mover = PLCMagnetMover()
        magnet_mover.go_to_position(x, y)
        return {'message': f'Moved to position ({x}, {y}) successfully'}

@ns.route('/report_location')
class ReportLocation(Resource):
    @ns.doc('report_location')
    def get(self):
        """Report the current location"""
        magnet_mover = PLCMagnetMover()
        location = magnet_mover.report_location()
        return {'location': location}

@ns.route('/report_error_margin')
class ReportErrorMargin(Resource):
    @ns.doc('report_error_margin')
    def get(self):
        """Report the error margin"""
        magnet_mover = PLCMagnetMover()
        error_margin = magnet_mover.report_error_margin()
        return {'error_margin': error_margin}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
