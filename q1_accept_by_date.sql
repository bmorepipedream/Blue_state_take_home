--case statement to calcualte the average of the # of accepted requests
--join table on itself to compare sent request to accepted requests
--group by 1 since there are only two dates that requests were sent


select 
rs.date as date_sent,AVG(case when ra.action ='accepted' then 1 else 0 end ) as percentage_accepted
from fb_friend_requests rs
left join fb_friend_requests ra
on rs.user_id_sender=ra.user_id_sender
and ra.action ='accepted'
where rs.action='sent' 
group by 1;