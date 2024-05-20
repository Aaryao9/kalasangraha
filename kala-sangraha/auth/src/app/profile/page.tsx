"use client"
import React from 'react'
import axios from 'axios'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { set } from 'mongoose'
import { get } from 'http'



function Profile() {

    const router = useRouter()
    const [data, setData] = React.useState<any>(null)

    const handleLogout = async (e:React.MouseEvent<HTMLButtonElement>) => {
        e.preventDefault()
        try {
            await axios.get('/api/users/logout')
            router.push('/login')
        } catch (error:any) {   
            console.log(error.message)
        }
    }

    const getUser = async () => {
        try {
            const jwt = {
                jwt: document.cookie.split('=')[1]
            }
            const res = await axios.get(process.env.NEXT_PUBLIC_PROFILE_URL!,{
                params:jwt,
            })
            console.log(res.data)
            setData(res.data.email)
        } catch (error:any) {
            console.log(error.message)
        }
    }
    getUser()


  return (
    <div>
        <div>Profile</div>
        <h1>{data===null ? "Nothing":<Link
        href={`/profile/${data}`}
        >
        visit profile
        </Link>}</h1>
        <button
            className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'
            onClick={handleLogout}
        >Log Out</button>

    </div>

  )
}

export default Profile