from flask import Blueprint, request, jsonify

sustainability_bp = Blueprint('sustainability_bp', __name__)

sustainability_reports = {
    1: {"initiative": "Eco-Friendly Packaging", "impact": "Reduced plastic by 60%"},
    2: {"initiative": "Carbon-Neutral Shipping", "impact": "Offset 100 tons CO2"}
}

# GET /sustainability - get all reports
@sustainability_bp.route('/sustainability', methods=['GET'])
def get_all_sustainability():
    return jsonify(list(sustainability_reports.values()))

# GET /sustainability/<id> - get one report
@sustainability_bp.route('/sustainability/<int:report_id>', methods=['GET'])
def get_sustainability_report(report_id):
    report = sustainability_reports.get(report_id)
    if report:
        return jsonify(report)
    return jsonify({"error": "Report not found"}), 404

# POST /sustainability - new report
@sustainability_bp.route('/sustainability', methods=['POST'])
def create_sustainability_report():
    data = request.json
    new_id = max(sustainability_reports.keys()) + 1
    sustainability_reports[new_id] = data
    return jsonify({"message": "Sustainability initiative added", "id": new_id}), 201

# PUT /sustainability/<id> - update an initiative
@sustainability_bp.route('/sustainability/<int:report_id>', methods=['PUT'])
def update_sustainability_report(report_id):
    if report_id in sustainability_reports:
        sustainability_reports[report_id].update(request.json)
        return jsonify({"message": "Sustainability initiative updated"})
    return jsonify({"error": "Report not found"}), 404

# DELETE /sustainability/<id> - delete an initiative
@sustainability_bp.route('/sustainability/<int:report_id>', methods=['DELETE'])
def delete_sustainability_report(report_id):
    if report_id in sustainability_reports:
        del sustainability_reports[report_id]
        return jsonify({"message": "Sustainability initiative deleted"})
    return jsonify({"error": "Report not found"}), 404

# GET /sustainability/impact - view overall environmental impact
@sustainability_bp.route('/sustainability/impact', methods=['GET'])
def get_overall_impact():
    total_initiatives = len(sustainability_reports)
    return jsonify({
        "total_initiatives": total_initiatives,
        "message": "Positive environmental changes recorded."
    })

# POST /sustainability/audit - submit an audit
@sustainability_bp.route('/sustainability/audit', methods=['POST'])
def submit_audit():
    data = request.json
    # Normally you would process/save this audit data
    return jsonify({"message": "Audit submitted successfully", "audit_details": data}), 201
