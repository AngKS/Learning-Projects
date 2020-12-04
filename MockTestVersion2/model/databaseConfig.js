
// Author: Ang Kah Shin

var mysql = require('mysql');

var dbConnect = {
    getConnection:function(){
        var conn = mysql.createConnection({
            host : "localhost",
            user : "",
            password : "",
            database : "food_db"
        }
        );
        return conn;
    }
}
module.exports=dbConnect;
