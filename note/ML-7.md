# ML Lecture 7: Backpropagation

> 臺灣大學人工智慧中心 科技部人工智慧技術暨全幅健康照護聯合研究中心 [http://ai.ntu.edu.tw](http://ai.ntu.edu.tw/)

### Gradient Descent

- Backpropagation 就是 Gradient Descent，但 Backpropagation 是較有效率的演算法
- 詳見 ML 3-1 Gradient Descent 複習（https://youtu.be/yKKNr-QKz2Q）

<img src="http://ai.ntu.edu.tw/aho/JPG/Backpropagation/Backpropagation_1.jpg" width="70%">

### Chain Rule

- **Case 1**

  > 有兩個 function，**y = g(x)** 、 **z = h(y)**
  > => (output) x 的微小變化，會影響到 z 
  > => (微分) dz/dx = dz/dy * dy/dx 

- Case 2

  > 有三個 function，**x = g(s)** 、 **y = h(s)**、 **z = k(x,y)**
  >
  > => (output) 改變 s，影響到 x 跟 y，最後影響 z
  >
  > => (微分可拆成兩項) $\frac{dz}{ds} = \frac{∂z}{∂x} \frac{dx}{ds} + \frac{∂z}{∂y} \frac{dy}{ds}$

<img src="http://ai.ntu.edu.tw/aho/JPG/Backpropagation/Backpropagation_2.jpg" width="70%">

## Backpropagation

### Loss function

- Loss 來源：
  給定一組 Neural Network 的參數 $θ$，將 training data, **x<sup>n</sup>** 代到 Neural Network 裡面，會 output **y<sup>n</sup>**，
  而 **y<sup>n</sup>** 和我們希望 output 的 **$\hat{y}^n$** 之間距離的 function 即為 **C<sup>n</sup>**
- Total Loss：
  (計算)  $L(θ) = \sum\limits_{n=1}^N l^n(θ)$
  (微分) $$\frac{∂L(θ)}{∂w} = \sum\limits_{n=1}^N\frac{∂l^n(θ)}{∂w}$$

<img src="http://ai.ntu.edu.tw/aho/JPG/Backpropagation/Backpropagation_3.jpg" width="70%">

---

#### 簡化問題：$\frac{∂l}{∂w} = \frac{∂z}{∂w}\frac{∂l}{∂z} $ 

=> 某一筆 data 的 cost, **l** 對參數 w 的偏微分

(因為算出 $\frac{∂l}{∂w}$ 後，再 $\sum$ 所有 training data，就可以把$L(θ)$ 對某一參數的偏微分算出來了)

<img src="http://ai.ntu.edu.tw/aho/JPG/Backpropagation/Backpropagation_4.jpg" width="70%">
---

### Forward Pass：計算 $\frac{∂z}{∂w}$ 的過程

- 規律：z 對參數 w 偏微分的值，即為 w 前面所接 input 的值

  > Ex：$∂z / ∂w_1= x_1 $、$∂z / ∂w_2= x_2$ 

- 結論：
  要計算每個 weight, w 對 activation functon 的 input, z 的偏微分，
  丟進 input，計算每個 neuron 的 output，就結束了。

<img src="http://ai.ntu.edu.tw/aho/JPG/Backpropagation/Backpropagation_5.jpg" width="70%">

---

### Backward pass：計算 $\frac{∂l}{∂z}$ 的過程

假設：此處的 activation function 是 sigmoid function

$\frac{∂l}{∂z}$ 可以拆成 $\frac{∂a}{∂z}\times\frac{∂l}{∂a} $

1. 前項 ($\frac{∂a}{∂z}$) 就是 sigmoid function 的微分，$σ\prime(z)$，下圖中藍線所表示

<img src="http://ai.ntu.edu.tw/aho/JPG/Backpropagation/Backpropagation_7.jpg" width="70%">

2. 後項 ($\frac{∂l}{∂a}$) 可再拆成 $\frac{∂z\prime}{∂a}\frac{∂l}{∂z\prime} + \frac{∂z"}{∂a}\frac{∂l}{∂z"}$ (假設 a 之後只有兩個 neuron 的情況)

    $\frac{∂z\prime}{∂a}$ 和 $\frac{∂z"}{∂a}$ 即為 $w_3$ 和 $w_4$，$\frac{∂l}{∂z\prime}$ 和 $\frac{∂l}{∂z"}$ 假設已知

<img src="http://ai.ntu.edu.tw/aho/JPG/Backpropagation/Backpropagation_8.jpg" width="70%">

3. 故可推得 $\frac{∂l}{∂z} = σ\prime(z) [w_3\frac{∂l}{∂z\prime} + w_4\frac{∂l}{∂z"}]$

4. 求出 $\frac{∂l}{∂z\prime}$ 及 $\frac{∂l}{∂z"}$，有兩種 case

   - **Case 1. Output Layer**：
     紅色 neuron 後，即為 output layer (整個 neural network 的 output)

     > $\frac{∂l}{∂z\prime}$ = $\frac{∂y_1}{∂z\prime} \frac{∂l}{∂y_1}$
     >
     > $\frac{∂l}{∂z"}$ = $\frac{∂y_2}{∂z} \frac{∂l}{∂y_2}$

   <img src="http://ai.ntu.edu.tw/aho/JPG/Backpropagation/Backpropagation_11.jpg" width="70%">

   - **Case 2. Not Output Layer**：
     繼續往下層 layer 走，走到 output layer，再從 output layer 反算回來

     > 如下圖，從 $z_5、z_6$ 的的偏微分算回 $z_3、z_4$ 到 $z_1、z_2$

     <img src="http://ai.ntu.edu.tw/aho/JPG/Backpropagation/Backpropagation_16.jpg" width="70%">

---

### Summarize

1. Forward Pass，算出每個 activation function 的 output (即為它所連接的 weight 的 $\frac{∂z}{∂w}$)
2. Backward Pass，將原來的 neural network 反向(如下圖)，每個三角形的 output 就是 $\frac{∂l}{∂z}$
3. 最後，兩者相乘即得 $\frac{∂l}{∂w}$

<img src="http://ai.ntu.edu.tw/aho/JPG/Backpropagation/Backpropagation_17.jpg" width="70%">