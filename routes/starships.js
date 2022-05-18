
import { Router } from 'express'
import * as starshipsCtrl from '../controllers/starships.js'
import { decodeUserFromToken, checkAuth } from '../middleware/auth.js'

const router = Router()

/*---------- Public Routes ----------*/
router.get('/', starshipsCtrl.index)


/*---------- Protected Routes ----------*/
router.use(decodeUserFromToken)
router.post('/', checkAuth, starshipsCtrl.create)
router.put('/:id', checkAuth, starshipsCtrl.update)
router.patch('/:id', checkAuth, starshipsCtrl.patchOne)
router.delete('/:id', checkAuth, starshipsCtrl.deleteShip)

export { router }
