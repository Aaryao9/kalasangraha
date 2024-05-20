import Image from "next/image";
import Navbar from "../components/navbar";
import BestSeller from "../components/bestseller";
import Slider from "../components/slider";
import { Roboto } from "next/font/google";

export default function Home() {
  return (
  <>
      <Navbar/>
      
        <Slider/>
      
      <div className="font-roboto font-bold h-[200px] ">Our bestsellers
      <div className="flex col items-center justify-between p-[10px]">
        <BestSeller/>
        <BestSeller/>
        <BestSeller/>
        <BestSeller/>
      </div> 
      </div>
   </>
  );
}
