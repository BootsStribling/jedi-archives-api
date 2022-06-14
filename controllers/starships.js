import { Starship } from '../models/starships/individualStarship.js'

const ips = new Map()

function index(req, res) {
  if(ips.has(req.ip)){
    ips[req.ip] += 1
  }else{
    ips[req.ip] = 1
  }
  Starship.find({})
  .then(starships => {
    if(starships.length > 0) res.json({starships, msg: `Is this what you're looking for?`})
    if(starships.length === 0) res.json({starships, msg: `No starships`})
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
    if(starships.length === 0) res.json({msg: `No starships match your query. Adjust your query.`})
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
    console.log(err, `Error deleting with ${req.body}`)
    res.status(500).json({err, msg: `ERR:Deletingwithquery \n These aren't the droids your looking for.`})
  })
}

//SORT takes in the request body and prioritizes sort order based on priority in the request body.
  //For example - if your body looks like this:
    /*{
      "length": "asc",
      "width": "desc"
    }
  Sort will prioritize length sorting first and then within ships of the same length, will prioritze width sorting within the ships that have the same length
  //
      */
function sort(req,res){
  console.log(req.params, "req.params")
  Starship.find(req.params.query).sort(req.body)
  .then(starships => res.json({starships, msg: `Is this how you wanted them ordered, sir?`}))
  .catch(err => {
    console.log(err, `Error sorting with query ${req.params.query}`)
    res.status(500).json({err, msg:`ERR:Sort \n I can't seem to make out what you're asking me!`})
  })
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
  .then(starship => res.status(200).json({msg: `Destroyed the ${starship.name}. \n Watch your back.`}))
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



console.log(ips)