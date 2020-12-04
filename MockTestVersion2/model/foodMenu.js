var db = require('./databaseConfig.js');

// Author: Ang Kah Shin

const foodMenu = {

    // GET Request
    getAllFood : (callback) => {
        const dbConnect = db.getConnection()
        dbConnect.connect((err) => {
            if (err){
                console.log('Connection Error!')
                return callback(err, null)
            }
            else{
                let allFoodMenuQUERY = "SELECT * FROM foodmenu"
                dbConnect.query(allFoodMenuQUERY, (err, result) => {
                    dbConnect.end()
                    if (err){
                        console.log('Query Error!')
                        return callback(err, null)
                    }
                    else{
                        console.log('Query Successful!')
                        return callback(null, result)
                    }
                })
            }
        })
    },

    // PUT Request
    updateFood : (name, description, price, food_id, callback) => {
        const dbConnect = db.getConnection()
        dbConnect.connect((err) => {
            if (err){
                console.log('Connection Error')
                return callback(err, null)
            }
            else{
                let addFoodQUERY = 'UPDATE foodmenu SET foodName = ?, foodDescription = ?, price = ? WHERE id=?'
                dbConnect.query(addFoodQUERY, [name, description, price, food_id], (err, result) => {
                    dbConnect.end()
                    if (err){
                        console.log('Query Error')
                        return callback(err, null)
                    }
                    else{
                        console.log('Query Successful!')
                        return callback(null, {"Affected Rows" : `${result.affectedRows}`})
                    }
                })
            }
        })
    },

    // DELETE Request
    deleteFood : (food_id, callback) => {
        const dbConnect = db.getConnection()
        dbConnect.connect((err) => {
            if (err){
                console.log('Connection Error')
                return callback(err, null)
            }
            else{
                let deleteFoodQUERY = "DELETE FROM foodmenu WHERE id = ?"
                dbConnect.query(deleteFoodQUERY, [food_id], (err, result) => {
                    dbConnect.end()
                    if (err){
                        console.log('Query Error')
                        return callback(err, null)
                    }
                    else{
                        console.log('Query Successful!')
                        return callback(null, {"Affected Rows" : `${result.affectedRows}`})
                    }
                })
            }
        })
    },

    // INSERT Request
    addFood : (name, description, price, callback) => {
        const dbConnect = db.getConnection()
        dbConnect.connect((err) => {
            if (err){
                console.log('Connection Error')
                return callback(err, null)
            }
            else{
                let addFoodQUERY = "INSERT INTO foodmenu (foodName, foodDescription, price) VALUES (?, ?, ?)"
                dbConnect.query(addFoodQUERY, [name, description, price], (err, result) => {
                    dbConnect.end()
                    if (err){
                        console.log('Query Error!')
                        return callback(err, null)
                    }
                    else{
                        console.log('Query Successful!!')
                        return callback(null, "Successfully added a new item to the food menu!")
                    }
                })
            }
        })
    }
}

module.exports = foodMenu