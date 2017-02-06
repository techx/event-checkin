from checkin import app

app.config.update(
    PRINTER_NAME="DYMO_LabelWriter_450_Turbo",
    LABEL_WIDTH=760,
    LABEL_HEIGHT=410,
    debug=True
)

if __name__ == "__main__":
    app.run(debug=True)
