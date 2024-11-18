from flask import Flask, jsonify, request

app = Flask(__name__)


def get_color(risk_percentage):
    """
    Maps a risk percentage (0-100) to a color.
    Low risk      (0)   -> Green  (#00FF00)
    Moderate risk (50)  -> Yellow (#FFFF00)
    High risk     (100) -> Red    (#FF0000)
    """
    if risk_percentage <= 50:
        red = int((risk_percentage / 50) * 255)
        green = 255
        blue = 0
    else:
        red = 255
        green = int(((100 - risk_percentage) / 50) * 255)
        blue = 0

    return f"#{red:02X}{green:02X}{blue:02X}"


@app.route("/risk-color", methods=["POST"])
def risk_color():
    try:
        data = request.get_json()
        if "risk" not in data:
            return jsonify({"error": "Missing 'risk' key in JSON payload"}), 400

        risk_percentage = data["risk"]

        if not isinstance(risk_percentage, (int, float)):
            return jsonify({"error": "Risk must be a number"}), 400

        color = get_color(risk_percentage)
        return jsonify({"risk": risk_percentage, "color": color})

    except Exception as e:
        return jsonify({"error": "An error occurred", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
