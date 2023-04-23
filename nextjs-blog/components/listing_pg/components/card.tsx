import React from "react" 
import st from "../../../styles/listing_pg/card.module.css"
import Link from "next/link";
import { useDispatch, useSelector } from "react-redux";
export default function Card(props) { 
    // const { isLoggedIn} = useSelector(
    //     (state: RootState) => state.storage
    //   );
    let obj = props.obj 
    return (
                
    //     <Link href={"/about"} passHref>
    //     <div className={st.dropbtn}><p className={st.navText}>{"About Us"}</p></div>
    //   </Link>
                
                <div className= {st.card_container} >
                    <img src = {obj.product_img_url} className= {st.card_img1} />
                    
                    <div className= {st.details1} >
                        <img src = {obj.company_img_url} className= {st.card_img2} />
                        <div className= {st.contractor_div} >
                            <div className={st.contractor}>
                                {obj.contractor_name} 
                            </div>
                            
                        </div>
                        <button className= {st.btn} onClick={props.clicker}>Connect</button>
                    </div>
                    <div className={st.details2}>
                        {obj.description}
                    </div>
                </div>
    )
} 