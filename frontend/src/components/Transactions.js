import axios from 'axios';
import React, { useState, useEffect } from 'react'
import Stock from './Stock';
import { TextField, Grid, Card, Paper, Box } from '@material-ui/core';

const Transactions = () => {

  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/stockwatch/transactions/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    }).then((res) => {
      console.log(res.data);
      const stocks = []
      res.data.forEach((item) => {
        stocks.push(item)
      })
      setTransactions(res.data)

    })
  }, [])

  /**
   example transaction object
  "id": 1,
    "amount": 1,
    "price": 146.1,
    "type": "buy",
    "date": "2022-10-05T04:12:10.414961Z",
    "account": 1,
    "stock": 1
   */
  return (
    <div>
      <h3>Transactions</h3>
      {transactions.map((transaction) => (
        <div key={transaction.id}>
          <p>{transaction.stock.name}</p>
          <p>{transaction.amount} shares of {transaction.stock.ticker} at {transaction.price} on {transaction.date}</p>
        </div>
      ))}
      <Box
      sx={{
        p: 2,
        display: 'grid',
        gap: 2,
        width: '10%',
      }}
      >
      {transactions.map((transaction) => (
        <Stock key={transaction.id}
          ticker={transaction.stock.ticker}
          amount={transaction.amount}
          price={transaction.price}
          name={transaction.stock.name}
          id={transaction.id}
        />
      ))}
      </Box>



    </div>
  )
}

export default Transactions