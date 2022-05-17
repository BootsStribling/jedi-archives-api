import mongoose from 'mongoose'
const ObjRef = mongoose.Schema.Types.ObjectId
const Schema = mongoose.Schema

const starshipSchema = new Schema({
  image: {
    //URL to non-dependent image- perhaps Cloudinary eventually
    type: String,
    default: null,
  },
  name: {
    //formatted for capital letters to start words of the name
    type: String,
    default: null,
  },
  manufacturer: {
    // formatted to allow capital letters of the name of manufacturer
    type: String,
    default: null,
  },
  line: {
    type: String,
    default: null,
  },
  model: {
    type: String,
    default: null,
  },
  class: {
    type: String,
    default: null,
  },
  cost: {
    type: Number,
    default: null,
  },
  modifier: {
    type: ObjRef, 
    ref: 'Individual'
  },
  
},{
    timestamps: true,
})

const Starship = mongoose.model('Starship', starshipSchema)

export {Starship}
