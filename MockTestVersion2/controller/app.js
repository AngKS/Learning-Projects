
// Author: Ang Kah Shin

var express=require('express');
var foodMenu = require('../model/foodMenu.js')
var bodyParser = require('body-parser');

var app = express();


var urlencodedParser = bodyParser.urlencoded({extended:false});

app.use(urlencodedParser);
app.use(bodyParser.json()); //parse appilcation/json data

app.get("/foodMenu", (req, res) => {
    foodMenu.getAllFood((err, result) => {
        if (err){
            console.log('Database Error')
            res.status(500).type("application/json").json({"Result": "Internal Server Error!"})
            
        }
        else{
            res.status(200).type("application/json").json(result)
        }
    })
})

app.put("/foodMenu/:foodID", (req, res) => {
    let food_id = req.params.foodID
    let foodName = req.body.foodName
    let foodDesc = req.body.foodDesc
    let foodPrice = req.body.price

    foodMenu.updateFood(foodName, foodDesc, foodPrice, food_id, (err, result) => {
        if (err){
            console.log('Database Error')
            res.status(500).type("application/json").json({ "Result": "Internal Server Error!" })
        }
        else{
            res.status(201).type("application/json").json(result)
        }
    })
})

app.delete("/foodMenu/:foodID", (req, res) => {
    let food_id = req.params.foodID
    foodMenu.deleteFood(food_id, (err, result) => {
        if (err){
            console.log('Database Error')
            res.status(500).type("application/json").json({ "Result": "Internal Server Error!" })
        }
        else{
            res.status(201).type("application/json").json(result)
        }

    })
})

app.post("/foodMenu", (req, res) => {
    let foodName = req.body.foodName
    let foodDesc = req.body.foodDesc
    let price = req.body.price
    foodMenu.addFood(foodName, foodDesc, price, (err, result) => {
        if (err){
            console.log('Database Error')
            res.status(500).type("application/json").json({ "Result": "Internal Server Error!" })
        }
        else{
            res.status(201).type("text/html").end(result)
        }
    })
})


// If all fails/no file found, fallback to this middleware
app.use((req, res) => {
    // Another way of indenting the status/type/endpoint
    res.status(404).type('text/html').end("<html><body><h1>Error 404</h1><p>File not found!</p></body></html>");
});

module.exports=app;