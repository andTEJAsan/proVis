import PageTemplate from "../../components/reusable/template/PageTemplate.tsx";
import st from "./contact.module.scss";

export default function Bookmarks() {
  return (
    <PageTemplate outsideApp>
      <div className={st.mainContainer}>
        <div>
          <h1>Contact proVis</h1>
          <p>Let's discuss how we can help you!</p>
        </div>
        <div>
          {contactData.map((data, index) => (
            <div key={index}>
              <img src={data.imgUrl} />
              {data.type == "email" ? (
                <a href={`mailto:${data.desc}`}>{data.desc}</a>
              ) : data.type == "phone" ? (
                <a href={`tel:${data.desc}`}>{data.desc}</a>
              ) : (
                <p>{data.desc}</p>
              )}
            </div>
          ))}
        </div>
      </div>
    </PageTemplate>
  );
}
