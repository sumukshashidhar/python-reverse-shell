module.exports = function(app) {
    app.get('/', function(res) {
        res.status(200).json({
            "message":"All OK"
        });
    });
}
