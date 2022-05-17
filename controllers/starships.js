import { Starship } from '../models/starship.js'

function index(req, res) {
  Starship.find({})
  .then(starships => res.json(starships))
  .catch(err => {
    console.log(err)
    res.status(500).json(err)
  })
}

function create(req,res){
  Starship.create(req.body)
  .then(starship => res.status(201).json(starship))
  .catch(err => {
    console.log(err)
    res.status(500).json(err)
  })
}

export { 
  index,
  create,
}
