export default function handler(req, res) {
    res.status(200).json({ access_token: '123', refresh_token: '456' });
}

// export default function handler(req, res) {
//     res.status(200).json({ name: 'John Doe' });
// }
