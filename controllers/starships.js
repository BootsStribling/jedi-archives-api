import { Starship } from '../models/starship.js'

function index(req, res) {
  Starship.find({})
  .then(starships => {
    if(starships.length > 0) res.json({starships, msg: `Is this what you're looking for?`})
    if(starships.length === 0) res.json({starships, msg: `Nothing found.`})
  })
  .catch(err => {
    console.log(err, 'Error finding all the starships.')
    res.status(500).json({err, msg: `ERR:Indexing \n I can't see 'em! Pick up your visual scanning!`})
  })
}

function findWithQuery(req,res){
  Starship.find(req.body)
  .then(starships => {
    if(starships.length > 0) res.json({starships, msg: `The fleet is arriving!`})
    if(starships.length === 0) res.json({starships, msg: `Where is everybody?`})
  })
  .catch(err => {
    console.log(err, `Error finding with Queries ${req.body}`)
    res.status(500).json({err, msg: `ERR:Querying \n He can go about his business. ${req.body} queries didn't return anything or are improperly formatted as a object.`})
  })
}

function show(req,res){
  Starship.findById(req.params.id)
  .then(starship => res.status(200).res.json({starship, msg: `My Lord, we've found them.`}))
  .catch(err => {
    console.log(err, `Error finding with Id ${req.params.id}`)
    res.status(500).json({err, msg: `ERR:Show \n You have failed me for the last time, Admiral. Didn't find anything with that Id ${req.params.id}`})
  })
}

//Delete on Query takes anything that is in the body and deletes based on those parameters
function deleteMany(req,res){
  Starship.deleteMany(req.body)
  .then(casualties => res.json({casualties, msg: `We've destroyed the whole fleet! \n Lets's get out of here!`}))
  .catch(err => {
    console.log(err, `Error deleting with ${req.params.query}`)
    res.status(500).json({err, msg: `Err:Deletingwithquery \n These aren't the droids your looking for.`})
  })
}

function sort(req,res){
  Starship.find(req.body).sort({field: `${req.params.query}`})
}

function create(req,res){
  Starship.create(req.body)
  .then(starship => res.status(201).json({starship, msg: `${starship.name} has completed construction. \n May the force be with you.`}))
  .catch(err => {
    console.log(err, 'Error creating starship.')
    res.status(500).json({err, msg: `ERR:Creating \n Bzzzt! Manufacture error! Recalibrate and try again.`})
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
  .then(starship => res.status(200).json({msg: `Destroyed ${starship.name}. \n Watch your back.`}))
  .catch(err=> {
    console.log(err, 'Error deleting ship.')
    res.status(500).json({err, msg: `ERR:Deleting \n Those shields are too strong for blasters! \n Get your harpoons and tow-cables and come back on follow me on the next pass!`})
  })
}

export { 
  index,
  findWithQuery,
  show,
  sort,
  create,
  update,
  deleteShip,
  deleteMany
}
