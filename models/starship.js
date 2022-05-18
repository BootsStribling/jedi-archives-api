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
  modifier: [{
    type: ObjRef, 
    ref: 'Individual'
  }],
  sysMods: [{
    type: String,
  }],
  length: {
    type: Number,
    default: null,
  },
  width: {
    type: Number,
    default: null,
  },
  height: {
    type: Number,
    default: null,
  },
  mass: {
    type: Number,
    default: null,
  },
  maxAccel: {
    type: Number,
    default: null,
  },
  mglt: {
    type: Number,
    default: null,
  },
  maxSpeed: {
    type: Number,
    default: null,
  },
  maneuverability: {
    type: Number,
    default: null,
  },
  engineType: {
    type: String,
    default: null,
  },
  engineNo: {
    type: Number,
    default: null,
  },
  hyperdrive: [{
    type: String,
  }],
  hyperDriveRtg: {
    type: Number,
  },
  hyperdriveRnge: {
    type: Number,
    default: null,
  },
  powerplant: [{
    type: String,
  }],
  powerOutput: {
    type: String,
    default: null,
  },
  shields: [{
    type: String,
  }],
  hull: [{
    type: String,
  }],
  sensorSys: [{
    type: String,
  }],
  targetSys: [{
    type: String,
  }],
  navSys: [{
    type: String,
  }],
  avionics: [{
    type: String,
  }],
  mainComp: [{
    type: String,
  }],
  counterMeasures: [{
    type: String,
  }],
  armament: [{
    type: String,
  }],
  complement: [{
    type: String,
  }],
  bays: {
    type: Number,
    default: null,
  },
  escapePods: [{
    type: String,
  }],
  escapePodNo: {
    type: Number,
    default: null,
  },
  crewRoles: [{
    type: String,
  }],
  minCrew: {
    type: Number,
    default: null,
  },
  passengers: {
    type: Number,
    default: null,
  },
  cargoCap: {
    type: Number,
    default: null,
  },
  cargoHandlingSys: [{
    type: String,
  }],
  consumables: {
    type: Number,
    default: null,
  },
  lifeSupportSys: [{
    type: String,
  }],
  commSys: [{
    type: String,
  }],
  auxSys: [{
    type: String,
  }],
  availability: {
    type: Boolean,
    default: false,
  },
  roles: [{
    type: String,
  }],
  manufactureDate: {
    type: Number,
    default: null,
  },
  manufactureDateSuffix: {
    type: String,
    default: null,
    enum: ['ABY', 'BBY', null]
  },
  destroyedDate: {
    type: Number,
    default: null,
  },
  destroyedDateSuffix: {
    type: String,
    default: null,
    enum: ['ABY', 'BBY', null]
  },
  retiredDate: {
    type: Number,
    default: null,
  },
  retiredDateSuffix: {
    type: String,
    default: null,
    enum: ['ABY', 'BBY', null]
  },
  battles: [{
    type: String,
  }],
  affiliations: [{
    type: String,
  }],
  navy: [{
    type: String,
  }],
  fleet: [{
    type: String,
  }],
  owners: [{
    type: ObjRef, 
    ref: 'Individual'
  }],
  captains: [{
    type: ObjRef, 
    ref: 'Individual'
  }],
  crewMembers: [{
    type: ObjRef, 
    ref: 'Individual'
  }],
  regNo: [{
    type: String,
  }],
  regDate: {
    type: Number,
    default: null,
  },
  regDateSuffix: {
    type: String,
    default: null,
    enum: ['ABY', 'BBY', null]
  },
  aliases: [{
    type: String,
  }],
  tags: [{
    type: String,
  }],
  canon: {
    type: String,
    enum: ['Canon', 'Legends', null],
    default: null,
  },
  outOfUniverse: {
    type: Boolean,
    default: true,
  },
  refs: [{
    type: String,
  }],
},{
    timestamps: true,
})

const Starship = mongoose.model('Starship', starshipSchema)

export {Starship}
