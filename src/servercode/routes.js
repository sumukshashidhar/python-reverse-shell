module.exports  = function(app) {
    require('./routes/test_routes.js')(app);
    require('./routes/main_routes.js')(app);
};
