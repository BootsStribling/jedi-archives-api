
import { Router } from 'express'
import * as starshipsCtrl from '../controllers/starships.js'
import { decodeUserFromToken, checkAuth } from '../middleware/auth.js'

const router = Router()

/*---------- Public Routes ----------*/
router.get('/', starshipsCtrl.index)
router.get('/:id', starshipsCtrl.show)
router.get('/?=', starshipsCtrl.findWithQuery)
router.get('/?=:query', starshipCtrl.sort)


/*---------- Protected Routes ----------*/
router.use(decodeUserFromToken)
router.post('/', checkAuth, starshipsCtrl.create)
router.put('/:id', checkAuth, starshipsCtrl.update)
router.delete('/', checkAuth, starshipsCtrl.deleteMany)
router.delete('/:id', checkAuth, starshipsCtrl.deleteShip)

export { router }
