const authService = require("../services/auth.service")
const Token = require("../models/token.schema")
const SECRET = process.env.SECRETKEY

const register = async (req, res) => {
      try{
            const {email, password, role} = req.body
            const user = await authService.register(email, password, role)
            res.json({message: "User registed", user})
      }catch(err){
            res.status(400).json({error: err.message})
      }
}

const login = async (req, res) => {
      try{
            const {email, password} = req.body
            const {user, token} = await authService.login(email, password, SECRET);
            res.json({message: "Login success", token, user})
      }catch(err){
            res.status(401).json({error: err.message})
      }
}

const logout = async (req, res) => {
      try{
            const token = req.headers.authorization.split(" ")[1];
            await authService.logout(token)
            res.json({ message: "Logged out" });
      }catch(err){
            res.status(401).json({error: err.message})
      }
}

const authenticate = async (req, res, next) => {
      try{
            const token = req.headers.authorization?.split(" ")[1]
            if(!token) return res.status(401).json({error: "No token provided"})

            const payload = authService.verifyToken(token, SECRET)
            if(!payload) return res.status(401).json({error: "Invalid token"})

            const revoked = await authService.isTokenRevoked(token)
            if(revoked) return res.status(401).json({error: "Token revoked"})

            req.user = payload
            next()
      }catch(err){
            res.status(500).json({ error: err.message });
      }
}

const adminOnly = (req, res, next) => {
      if(req.user.role !== "admin") return res.status(403).json({error: "Forbidden"})
      next()
}

module.exports = {
      register, login, logout, authenticate, adminOnly
}