var mysql = require('mysql')

var con = mysql.createConnection({
    host: "5.183.188.132",
    //port: 8888,
    user: "db_vgu_student",
    password: "thasrCt3pKYWAYcK",
    database: "db_vgu_test"
})

con.connect(function(err){
    if (err) throw err;
    console.log("Connected!")
    con.query(`SELECT * FROM coupon;`, function(err, result){
        if (err) throw err;
        console.log("Result: "+result)
    })
})