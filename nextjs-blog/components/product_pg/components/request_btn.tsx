import React from "react" 
import * as Dialog from "@radix-ui/react-dialog";
import { Cross2Icon } from "@radix-ui/react-icons";
import st from "../../../styles/product_pg/request_btn.module.css"
import { useDispatch, useSelector } from "react-redux";
import config from "../../../config";
import {RootState} from "../../../redux/reducers"

export default function Request_Btn(props) {
  let [msgState, statehandler] = React.useState("") 




  function getCurrentDateTimeString() {
    const now = new Date();
    const year = now.getUTCFullYear();
    const month = now.getUTCMonth() + 1;
    const day = now.getUTCDate();
    const hours = now.getUTCHours();
    const minutes = now.getUTCMinutes();
    const seconds = now.getUTCSeconds();
    const milliseconds = now.getUTCMilliseconds();
  
    // Zero-pad month, day, hours, minutes, and seconds to two digits
    const zeroPad = (num) => num.toString().padStart(2, '0');
    const monthStr = zeroPad(month);
    const dayStr = zeroPad(day);
    const hoursStr = zeroPad(hours);
    const minutesStr = zeroPad(minutes);
    const secondsStr = zeroPad(seconds);
  
    // Format the date-time string
    const dateTimeStr = `${year}-${monthStr}-${dayStr}T${hoursStr}:${minutesStr}:${secondsStr}.${milliseconds}Z`;
    
    return dateTimeStr;
  }


  const request_body = {
    
    "order_date_time": "2023-04-07T13:13:20.235Z",
    "p_uid": props.p_id, 
    "cus_uid" : "ff" ,  
    "message" : "string"
  }

  // {
  //   "id": "vycs78",
  //   "cus_uid": "vycs78",
  //   "order_date_time": "2023-04-23T14:07:45.946Z",
  //   "p_uid": "vycs78",
  //   "message": "string"
  // }

  function handleChange(event) {
    let msg = event.target.value ;statehandler(msg) 
  }

  const { isLoggedIn} = useSelector(
    (state: RootState) => state.storage
  );
  
  // const jwt = useSelector((state) => state.storage.jwt);
  async function handleSubmit(event){ 
    if (isLoggedIn){
              const queryid = useSelector((state : RootState) => state.storage.userID)

                const { apiUrl } = config;

                request_body.order_date_time =  getCurrentDateTimeString()
                request_body.message = msgState ;
                request_body.cus_uid = queryid 
                const response = await fetch(`${apiUrl}/api/customers/${queryid}/orders`, {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json"
                    // Authorization: `Bearer ${jwt}`,
                  },
                  body: JSON.stringify(request_body) 
                });

                if (response.ok) {
                  console.log("response worked!");
                  statehandler("") 
                }
      }
      else{
        alert("log in first")
      }
    }

  

  return (
    <div className={st.DialogRoot}>
      <Dialog.Root  >
        <Dialog.Trigger asChild>
          <div className={st.button_wrapper}>
            <h3>Connect with the contractor</h3>
            <button className={st.Button}>
              {props.btn_text}
            </button>
          </div>
        </Dialog.Trigger>
        <Dialog.Portal>
          <Dialog.Overlay className={st.DialogOverlay} />
          <Dialog.Content className={st.DialogContent}>
            <Dialog.Title className={st.DialogTitle}>
              {props.modal_header}
            </Dialog.Title>
            <Dialog.Description className={st.DialogDescription}>
              {props.modal_description}
            </Dialog.Description>
            <fieldset className={st.Fieldset}>
              <label className={st.Label} htmlFor="msg">
                {props.label}
              </label>
              <input className={st.Input} id="name" defaultValue="" value = {msgState} onChange={handleChange}/>
            </fieldset>

            <div
              style={{
                display: "flex",
                marginTop: 25,
                justifyContent: "flex-end",
              }}
            >
              <Dialog.Close asChild>
                <button className={st.Button} onClick={handleSubmit} >
                  {props.modal_btn_text}
                </button>
              </Dialog.Close>
            </div>
            <Dialog.Close asChild>
              <button className={st.IconButton} aria-label="Close">
                <Cross2Icon />
              </button>
            </Dialog.Close>
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
    </div>
  );
}
