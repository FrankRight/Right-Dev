// const header1 = document.querySelector('h1');


function gcd (a, b)
{
   let r;
   while (b>0)
   {
      r=a%b;
      a=b;
      b=r;
   }
   return a;
}

function rel_prime(phi)
{
   let rel=5;
   
   while (gcd(phi,rel)!=1)
      rel++;
   return rel;
}

function power(a, b)
{
   let temp=1, i;
   for(i=1;i<=b;i++)
      temp*=a;
    return temp;
}

function encrypt(N, e, M)
{
   let r,i=0,prod=1,rem_mod=0;
   while (e>0)
   {
      r=e % 2;
      if (i++==0)
         rem_mod=M % N;
      else
         rem_mod=power(rem_mod,2) % N;
      if (r==1)
      {
         prod*=rem_mod;
         prod=prod % N;
      }
      e=parseInt(e/2);
   }
   return prod;
}

function calculate_d(phi,e)
{
   let x,y,x1,x2,y1,y2,temp,r,orig_phi;
   orig_phi=phi;
   x2=1;x1=0;y2=0;y1=1;
   while (e>0)
   {
      temp=parseInt(phi/e);
      r=phi-temp*e;
      x=x2-temp*x1;
      y=y2-temp*y1;
      phi=e;e=r;
      x2=x1;x1=x;
      y2=y1;y1=y;
      if (phi==1)
      {
         y2+=orig_phi;
         break;
      }
   }
   return y2;
}

function decrypt(c, d, N)
{
   let r,i=0,prod=1,rem_mod=0;
   while (d>0)
   {
      r=d % 2;
      if (i++==0)
         rem_mod=c % N;
      else
         rem_mod=power(rem_mod,2) % N;
      if (r==1)
      {
         prod*=rem_mod;
         prod=prod % N;
      }
      d=parseInt(d/2);
   }
   return prod;
}


function openNew()
{
    let subWindow=window.open(
    "Output.htm", "Obj","HEIGHT=400,WIDTH=600,SCROLLBARS=YES");
    let p=parseInt(document.Input.p.value);
    let q=parseInt(document.Input.q.value);
    let M=parseInt(document.Input.M.value);
    let N=p * q;
    let phi=(p-1)*(q-1);
    let e=rel_prime(phi);
    let c=encrypt(N,e,M);
    let d=calculate_d(phi,e);
    subWindow.document.Output.N.value=N;
    subWindow.document.Output.phi.value=phi;
    subWindow.document.Output.e.value=e;
    subWindow.document.Output.c.value=c;
    subWindow.document.Output.d.value=d;
    subWindow.document.Output.M.value=decrypt(c,d,N);
}