'use client';
import React from "react";
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { it } from "node:test";


function BestSeller() {
  return (
        <div>
       


    <Card style={{ width: '21rem',
    boxShadow: '4px 2px 4px 2px rgba(0, 0, 0, 0.1)',
    
    height: '13rem',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',

     }}>
        

        <Card.Body className="p-[90px] pb-[10px] pt-[10px] h-[300px] w-[300px] flex flex-col items-center justify-center ">
  
    <img className="h-[160px] w-[200px] rounded-xl" src="/card.png" alt="card image"/>
    <Card.Title className="text-center">AARYA</Card.Title>
  
</Card.Body>

    </Card>
  

        
        </div>
        
    
    );
}
export default BestSeller;