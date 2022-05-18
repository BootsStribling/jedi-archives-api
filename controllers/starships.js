import { Starship } from '../models/starship.js'

function index(req, res) {
  Starship.find({})
  .then(starships => {
    if(starships.length > 0) res.json({starships, msg: `The fleet is arriving!`})
    if(starships.length === 0) res.json({starships, msg: `Where is everybody?`})
  })
  .catch(err => {
    console.log(err, 'Error finding all the starships.')
    res.status(500).json({err, msg: `ERR:Indexing I can't see 'em! Pick up your visual scanning!`})
  })
}

function deleteMany(req,res){
  console.log(req.body.name, 'req.body.name')
  Starship.deleteMany({name: req.body.name})
  .then(starships => res.json({starships, msg: `We've destroyed the whole fleet! Lets's get out of here!`}))
  .catch(err => {
    console.log(err, `Error deleting with ${req.params.query}`)
    res.status(500).json({err, msg: `Err:Deletingw/query These aren't the droids your looking for.`})
  })
}

function create(req,res){
  Starship.create(req.body)
  .then(starship => res.status(201).json({starship, msg: `${starship.name} has completed construction. May the force be with you.`}))
  .catch(err => {
    console.log(err, 'Error creating starship.')
    res.status(500).json({err, msg: `ERR:Creating Bzzzt! Manufacture error! Recalibrate and try again.`})
  })
}

function update(req,res){
  Starship.findByIdAndUpdate(req.params.id, req.body, {new: true})
  .then(starship => res.status(200).json({starship, msg: `Your modifications to ${starship.name} have been completed. Let's hope you knew what you were doing.`}))
  .catch(err => {
    console.log(err, 'Error updating starship.')
    res.status(500).json({err, msg: `ERR:Updating No no no! This one goes here, that one goes there. Got it! Switch it round and try that modification again!`})
  })
}

function deleteShip(req,res){
  Starship.findByIdAndDelete(req.params.id)
  .then(starship => res.status(200).json({msg: `Destroyed ${starship.name}. Watch your back.`}))
  .catch(err=> {
    console.log(err, 'Error deleting ship.')
    res.status(500).json({err, msg: `ERR:Deleting Those shields are too strong for blasters! Get your harpoons and tow-cables and come back on follow me on the next pass!`})
  })
}

export { 
  index,
  create,
  update,
  deleteShip,
  deleteMany
}
