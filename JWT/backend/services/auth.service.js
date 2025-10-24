const crypto = require('crypto');
const User = require("../models/user.schema")
const Token = require("../models/token.schema")

const base64urlEncode = (str) => {
  return Buffer.from(str).toString("base64").replace(/=/g, "").replace(/\+/g, "-").replace(/\//g, "_");
}

const base64urlDecode = (str) => {
  str = str.replace(/-/g, "+").replace(/_/g, "/");
  return Buffer.from(str, "base64").toString();
}

const signToken = (payload, secret, expiresInSec = 3600) => {
  const header = {
        "alg": "HS256",
        "typ": "JWT"
      }
  const exp = Math.floor(Date.now() / 1000) + expiresInSec
  const data = {...payload, exp}

  const headerEncoded = base64urlEncode(JSON.stringify(header))
  const payloadEncoded = base64urlEncode(JSON.stringify(data))
  const signature = crypto.createHmac("sha256", secret).update(`${headerEncoded}.${payloadEncoded}`).digest("base64").replace(/=/g, "").replace(/\+/g, "-").replace(/\//g, "_");
  const token = `${headerEncoded}.${payloadEncoded}.${signature}`
  return token;
}

const verifyToken = (token, secret) =>{
  const [headerEncoded, payloadEncoded, signature] = token.split(".")
    const checkSignature = crypto
    .createHmac("sha256", secret)
    .update(`${headerEncoded}.${payloadEncoded}`)
    .digest("base64")
    .replace(/=/g, "")
    .replace(/\+/g, "-")
    .replace(/\//g, "_");

    if(signature !== checkSignature){
      return null
    }
    const payload = JSON.parse(base64urlDecode(payloadEncoded))
    if(payload.exp < Math.floor(Date.now() / 1000)){
      return null
    }
    return payload
}

const register = async (email, password, role = "student") => {
  const exist = await User.findOne({email})
  if(exist) throw new Error("User already exists")
  const user = new User({email, password, role})
  await user.save();
  return user;
}

const login = async (email, password, secret) => {
  const user = await User.findOne({email, password})
  if(!user) throw new Error("Invalid credentials")
  const token = signToken({id: user._id, role: user.role}, secret)
  await Token.create({userId: user._id, token})
  return {user, token}
}


const logout = async () => {
  await Token.deleteOne({token})
}

const isTokenRevoked = async (token) => {
  const exists = await Token.findOne({token})
  return !exists
}
module.exports = {  
  register,
  login,
  logout,
  verifyToken,
  signToken,
  isTokenRevoked,
}