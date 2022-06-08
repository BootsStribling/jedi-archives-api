import mongoose from 'mongoose'

const Schema = mongoose.Schema

const profileSchema = new Schema({
  email: {
    type: String, 
    required: true, 
    lowercase: true, 
    unique: true},
  name: String,
  role: {type: Number, 
    required: true, 
    default: 100, 
  },
},{
    timestamps: true,
})

const Profile = mongoose.model('Profile', profileSchema)

export {Profile}
