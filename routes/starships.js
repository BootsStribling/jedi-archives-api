
import { Router } from 'express'
import * as starshipsCtrl from '../controllers/starships.js'
import { decodeUserFromToken, checkAuth } from '../middleware/auth.js'

const router = Router()

/*---------- Public Routes ----------*/
router.get('/', starshipsCtrl.index)
router.get('/?', starshipsCtrl.findWithQuery)
router.get('/sort', starshipsCtrl.sort)
router.get('/:id', starshipsCtrl.show)


/*---------- Protected Routes ----------*/
router.use(decodeUserFromToken)
router.post('/', checkAuth, starshipsCtrl.create)
router.delete('/', checkAuth, starshipsCtrl.deleteMany)
router.put('/:id', checkAuth, starshipsCtrl.update)
router.delete('/:id', checkAuth, starshipsCtrl.deleteShip)

export { router }
