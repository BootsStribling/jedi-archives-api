
import { Router } from 'express'
import * as starshipsCtrl from '../controllers/starships.js'
import { decodeUserFromToken, checkAuth } from '../middleware/auth.js'

const router = Router()

/*---------- Public Routes ----------*/
router.get('/', starshipsCtrl.index)


/*---------- Protected Routes ----------*/
router.use(decodeUserFromToken)
router.post('/', checkAuth,starshipsCtrl.create)

export { router }
