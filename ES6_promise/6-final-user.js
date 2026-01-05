import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userPr = signUpUser(firstName, lastName);
  const photoPr = uploadPhoto(fileName);

  const responses = await Promise.allSettled([userPr, photoPr]);

  return responses.map((res) => {
    if (res.status === 'fulfilled') {
      return {
        status: 'fulfilled',
        value: res.value,
      };
    }
    return {
      status: res.status,
      value: String(res.reason),
    };
  });
}
