import axios from 'axios'
import React, { useState, useEffect }   from 'react'
import Stock from './Stock'

const Watchlist = () => {

    
    const [stocks, setStocks] = useState([])

    // const useEffect = () => {
    //     axios.get('http://127.0.0.1:8000/api/stockwatch/watchlist/', {
    //         headers: {
    //             Authorization: `Bearer ${localStorage.getItem('token')}`
    //         }
    //     })
    //     .then(res => {
    //         console.log(res)
    //         console.log(res.data)
    //     })//set stocks to res.data
    //     .then((res) => {
    //         setStocks(res.data)
    //     })
    // }

    /**
     
     "id": 1,
        "ticker": "AAPL",
        "name": "Apple",
        "price": 0.0
     */

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/stockwatch/watchlist/', {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`
            }
        })
        .then(res => {
            console.log(res)
            console.log(res.data)
        })
        .then((res) => {
            setStocks(res.data)
        })
    }, []);

  return (
    <div>
    <h3>watchlist:</h3>
    
    <Stock ticker='ticker' price='price' name='name' id='id' />
        {stocks.map((stock) => (
            <Stock ticker={stock.ticker} price={stock.price} name={stock.name} id={stock.id} />
        ))}

    </div>
  )
}

export default Watchlist