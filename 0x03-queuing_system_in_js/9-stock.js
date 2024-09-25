import { createClient } from 'redis';
import {promisify} from 'util';
const express = require('express');
const client = createClient();
const listProducts = [{
  'id': 1,
  'name': 'Suitcase 250',
  'price': 100,
  'stock': 4
},
  {
    'id': 2,
    'name': 'Suitcase 450',
    'price': 100,
    'stock': 10
  },
  {
'id': 3,
    'name': 'Suitcase 650',
    'price': 350,
    'stock': 2
  },
  {
'id': 4,
    'name': 'Suitcase 1050',
    'price': 550,
    'stock': 5
  }]
function getItemById(id){
  return listProducts.find(product=>product.id === id);
}
function reserveStockById(itemId, stock){
  client.hset('items', itemId, stock);
}
const hgetAsync = promisify(client.hget).bind(client);
async function getCurrentReservedStockById(itemId){
  try{
   const reservedStockCount = await hgetAsync('items', itemId);
    if(!reservedStockCount){
      return 0;
    }
    else{
      return reservedStockCount;
    }
  }
  catch(err){
    console.error('Error man: ', err);
  }
}
const app = express();
app.listen(1245);
app.get('/list_products',(_, res)=>{
  res.json(listProducts.map(product=>{
    return {"itemId":product.id,"itemName":product.name,"price":product.price,"initialAvailableQuantity":product.stock};
  })).end();
});
app.get('/list_products/:itemId', async (req, res)=>{
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  const reservedStockCount = await getCurrentReservedStockById(itemId);
  if(item){
    res.json({"itemId":item.id,"itemName":item.name,"price":item.price,"initialAvailableQuantity":item.stock,"currentQuantity": item.stock- reservedStockCount}).end();
  }
  else{
    res.json({"status":"Product not found"}).end();
  }
})
app.get('/reserve_product/:itemId', async (req, res)=>{
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if(item){
    const currReservedStockCount =  await getCurrentReservedStockById(itemId);
    if(item.stock - currReservedStockCount < 1){
      res.json({"status":"Not enough stock available","itemId":1}
      ).end();
    }
    else{
      reserveStockById(itemId, currReservedStockCount + 1);
      res.json({"status":"Reservation confirmed","itemId":item.id}).end();
    }
  }
  else{
    res.json({"status":"Product not found"}).end();
  }
});
