import React from 'react';
import styles from '../styles/components/C3MemberCard.module.css';
import EmailIcon from '@material-ui/icons/Email';

const C3MemberCard = ({ data }) => {
  return (
    <div className={styles.teamCard}>
      <img
        className={styles.profileImage}
        src={data.profile_image}
        alt={data.name}
      />
      <div className={styles.cardContent}>
        <b style={{ margin: '0', fontSize: '1.5rem' }}>{data.name}</b>
        <br></br>
        <div className={styles.department}>
          <b>{data.department}</b>
        </div>
        <div className={styles.cardFooter}>
          <a href={`mailto:${data.email}`} className={styles.email}>
            <EmailIcon style={{ margin: '0 0.5rem' }} />
            {data.email}
          </a>
        </div>
      </div>
    </div>
  );
};

export default C3MemberCard;
