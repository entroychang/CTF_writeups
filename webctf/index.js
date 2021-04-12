/* === Imports === */
const fs = require('fs');
const express = require('express')
, session = require('express-session');
const db = require('./middlewares/db')
, auth = require('./middlewares/auth')
, pool = db.pool
, passport = auth.passport
, bcrypt = require('bcryptjs');

/* === ======= === */

/* === Passport setup === */
const app = express();
app.use(express.urlencoded({ extended: false }));
app.use(express.static(__dirname + '/static'));
app.use(session({
    secret: 'who cares', resave: false, saveUninitialized: false 
  }));
app.use(passport.initialize());
app.use(passport.session());
/* === ============= === */

app.get('/freeInvite' , (req, res) => { 
    res.sendFile(__dirname + '/static/freeInvite.html');
});

app.get('/invite' , (req, res) => { 
    res.sendFile(__dirname + '/static/invite.html');
});


app.post('/freeInvite', auth.isAuthenticated, (req, res) => {
    let query = {
        name: 'get-invites-bb',
        text: 'SELECT bugbounty, email FROM invites WHERE bugbounty = $1',
        values: [req.user.name]
    }
    pool.query(query, (err, table) => {
        if(err) {
            console.log('Error selecting bug bounty' + err);
            res.sendStatus(500);
        } else{
            //Check if there's more than one invite
            if(!(table.rows.length > 0)){
                query = {
                    name: 'free-invite',
                    text: 'INSERT INTO invites(bugbounty, email) VALUES($1, $2)',
                    values: [req.user.name, req.body.email]
                }
                pool.query(query, (err, table) => {
                    if(err) {   
                        console.log('Error when inserting invite: ' + err);
                        res.sendStatus(500);
                    } else{
                        res.redirect('/manageBB');
                    }
                });
            } else {
                //If there's more than one, forbid
                res.sendFile(__dirname + '/static/forbidden.html');
            }
        }
        
    });
});

app.post('/createBB', (req, res) => {
    //Check for password strength
    if(req.body.password.length < 8){
        res.send("Password is not strong enough")
    } else{
        const salt = bcrypt.genSaltSync(10);
        const hash = bcrypt.hashSync(req.body.password, salt);
        const query = {
            name: 'create-bb',
            text: 'INSERT INTO bugbounties(name, password) VALUES($1, $2)',
            values: [req.body.name, hash]
        }
        pool.query(query, (err, table) => {
            if(err) {

                console.log('Error when creating bug bounty' + err);
                //Catch duplicate usernames
                if(err.message.includes('duplicate')){
                    res.sendFile(__dirname + '/static/duplicate.html');
                } else{
                    res.sendStatus(500);
                }
            }
            else{
                res.redirect('/');
            }
        });
    }
});

//Passport login
app.post('/login', 
  passport.authenticate('local'),
  function(req, res) {
    res.redirect('/manageBB');
});

app.get('/manageBB', auth.isAuthenticated, (req, res) => {
    console.log(req.user);
    const query = {
        name: 'get-invites-bb',
        text: 'SELECT bugbounty, email FROM invites WHERE bugbounty = $1',
        values: [req.user.name]
    }
    pool.query(query, (err, table) => {
        if(err) {
            console.log('Error selecting bugbounty ' + err);
            res.sendStatus(500);
        } else{
            console.log(table.rows.length)
            //If there's more than one invite, give flag
            if(table.rows.length > 1){
                const flagF = fs.readFileSync('flag.txt', 'utf8').replace('\n','')
                res.send(flagF);
            } else {
                res.sendFile(__dirname + '/static/manageBB.html');
            }
        }
    });
});

app.listen(8080)