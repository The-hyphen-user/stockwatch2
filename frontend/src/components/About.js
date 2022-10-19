import React, { useState, useEffect } from 'react'

const About = () => {
  return (
    <div>

      <h3>About</h3>
      <p>Welcome to stock watch.
        the goal of this site is to enable people to practice stock trading with virtual money.

      </p>

      <div>
        <h4>things to know</h4>
        <p>

          there will be random users generated to compete against on the high scores. there names will start with -bot-
          <br></br>
          for example -bot-dan  or -bot-joe
          <br />
          when created they will buy stocks at random and then halt all trading.

        </p>
      </div>
      <div>
        <h4>how to play</h4>
        <p>
          you will be given $10,000 to start with. Your balance is the combined value of all your stocks and balance.
          <br/>
          Try to see how much money you are able to obtain.
        </p>
        <br />
      </div>
      <div>
      <h4>Issues</h4>
      <p>if you encounter any issue or suggestions please email me <a href="mailto:daniel.wamsher@gmail.com"><button>Email</button></a></p>
      </div>
    </div>
  )
}

export default About