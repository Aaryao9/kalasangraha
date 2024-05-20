'use client'
import Carousel from 'react-bootstrap/Carousel';
import Image from 'next/image';
import { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function Slider() {
    

    return (
    <div style= {{width:"100%",height:"300px",overflow: "hidden" }}>
    
    <Carousel  data-bs-theme="dark">
      <Carousel.Item interval={1000}>
        <img
          className="d-block w-100"
          src="/card.png"
          alt="First slide"
          style={{ height: "300px", objectFit: "cover" }}
        />
        <Carousel.Caption>
          <h5>First slide label</h5>
          <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item interval={1000}>
        <img
          className="d-block w-100"
          src="/card.png"
          alt="Second slide"
          style={{ height: "300px", objectFit: "cover" }}
        />
        <Carousel.Caption>
          <h5>Second slide label</h5>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item interval={1000}>
        <img
          className="d-block w-100"
          src="/card.png"
          alt="Third slide"
          style={{ height: "300px", objectFit: "cover" }}
        />
        <Carousel.Caption>
          <h5>Third slide label</h5>
          <p>
            Praesent commodo cursus magna, vel scelerisque nisl consectetur.
          </p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
    </div>
  );
}

export default Slider;