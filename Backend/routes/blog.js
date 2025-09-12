const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.send("Blog page from router")
});
router.get('/about', (req, res) => {
    res.send("About page from blog router")
});
router.get('/blogpost/:slug', (req, res) => {
    res.send(`This is blog post title ${req.params.slug}`)
})
module.exports = router;