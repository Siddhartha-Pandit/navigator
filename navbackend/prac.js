import * as React from 'react';
import Box from '@mui/material/Box';
import LinearProgress from '@mui/material/LinearProgress';

export default function LinearDeterminate() {
  let val = 0
    const [progress, setProgress] = React.useState(0);
    let [color, setColor] = React.useState({ r: 70,g:120,b:150 });
    React.useEffect(() => {
        const timer = setInterval(() => {
            setProgress((oldProgress) => {
                if (oldProgress === 100) {
                    return 0;
                }
                const diff = 25;
                return Math.min(oldProgress + diff, 100);
            });
            setColor((e)=>{
            val += 1;
            if val!=4{
              return {
                r:e.r+50,
                g:e.g+50,
                b:e.b+10
              };
              }
              else{
                return e
              }
            })
            
            return () => {
                clearInterval(timer);
            };
        },1000)
        }, []);

        return (
            <Box sx={{ width: '100%' }}>
                <LinearProgress color="inherit" style={{ height: '15px', color: `rgb(${color.r},${color.g},${color.b})`}} variant="determinate" value={progress} />
            </Box>
        );
    }