require('dotenv').config();
const express = require('express');
const path = require('path');
const cors = require('cors');
const serveIndex = require('serve-index');
const helmet = require('helmet');

const app = express();

app.use(cors({
  origin: '*', 
  methods: ['*'], 
  allowedHeaders: ['*']
}));

app.use(helmet({
  crossOriginResourcePolicy: false,
}));

const imagesPath = path.join(__dirname, 'public/imagenes');
app.use(
  '/images',
  express.static(imagesPath),
  serveIndex(imagesPath, { icons: true, view: 'details' }) 
);

const HOST = process.env.HOST || '127.0.0.1';
const PORT = process.env.PORT || 3000;

app.listen(PORT, HOST, () => {
  console.log(`Servidor corriendo en http://${HOST}:${PORT}`);
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Error en el servidor');
});