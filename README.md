# Image Upscaling Algorithms: A Comprehensive Study

Image upscaling is a crucial technique in the realm of digital image processing, especially in applications where enhancing the resolution of images is essential, such as in medical imaging, satellite imagery, and video streaming. In this repository, we delve into the performance analysis of various image upscaling algorithms, using a Python-based implementation to evaluate their effectiveness.

## Introduction to Image Upscaling

Image upscaling, also known as image super-resolution, is the process of increasing the resolution of an image while preserving its essential features and minimizing distortions. The goal is to produce a high-resolution (HR) image from a low-resolution (LR) input, which involves estimating the missing high-frequency details.

## Algorithms Under Study in Detail

In our study, we focus on four prominent image upscaling algorithms: EDSR, ESPCN, FSRCNN, and LAPSRN. Each of these algorithms has unique characteristics and approaches to the problem of image super-resolution.

### 1. EDSR (Enhanced Deep Super-Resolution)
- A deep learning-based approach that uses residual blocks for super-resolution.
- Known for its high-quality results, especially in terms of sharpness and detail preservation.

### 2. ESPCN (Efficient Sub-Pixel Convolutional Neural Network)
- A lightweight and efficient algorithm designed for real-time image upscaling.
- Utilizes sub-pixel convolution layers to directly increase the resolution of the input image.

### 3. FSRCNN (Fast Super-Resolution Convolutional Neural Network)
- An improvement over the earlier SRCNN model, focusing on increasing processing speed without sacrificing image quality.
- Suitable for applications where both speed and image quality are important.

### 4. LAPSRN (Laplacian Pyramid Super-Resolution Network)
- Based on the concept of the Laplacian pyramid, employing a coarse-to-fine approach for upscaling.
- Effective for larger upscaling factors, producing sharp and detailed images.

## Experimental Setup

Our experimental setup involves evaluating the performance of the selected image upscaling algorithms at different scaling factors. We use a Python-based implementation, leveraging the OpenCV library for image processing and super-resolution, along with other standard libraries for computing evaluation metrics.

### Image Dataset

- **Input Images**: The input image is sourced from a designated directory (`image_path`). We only have a single image of the resolution 1920x1080. For each experiment, we are downscaling the original image with the scale factor to create the input image and then using the input image to upscale using the algorithm.
- **Scaling Factors**: The algorithms are tested at different scaling factors, specifically x2, x3, x4, and x8. These factors represent the degree to which the image resolution is increased.

### Super-Resolution Algorithms

- **Model Loading**: For each algorithm, the corresponding pre-trained model is loaded from the specified path (`path`). The models are trained to upscale images by the respective scaling factors.
- **Upsampling**: The low-resolution input images are upscaled using the super-resolution algorithms. The output is a high-resolution image that is compared against a reference image for evaluation.

### Evaluation Metrics

The performance of each algorithm is assessed using three primary metrics:

- **PSNR (Peak Signal-to-Noise Ratio)**: Typically between 20 dB to 40 dB for image super-resolution. Higher values indicate better image quality.
- **MSE (Mean Squared Error)**: Dependent on the image size and pixel intensity range. Lower values are desirable, indicating smaller differences between the original and upscaled images.
- **SSIM (Structural Similarity Index)**: Ranges between -1 and 1, where 1 indicates perfect similarity. Higher values signify better structural and perceptual similarity to the original image.

## Results and Analysis

Our evaluation of the image upscaling algorithms (EDSR, ESPCN, FSRCNN, LAPSRN) across different scaling factors (x2, x3, x4, and x8) provides insights into their performance in terms of image quality and processing time. Below, we present a detailed analysis of the results:

### Original Image
![pexels-nhu-tran-1479465](https://github.com/SachinSamuel01/image_upscale_python/assets/121634881/8c32e96e-602c-4609-b7a2-d2b6ec904d4e)

### Outputs
Reduced the image size to by 1/2 then upscaled with a scale of 2X
![X2](https://github.com/SachinSamuel01/image_upscale_python/assets/121634881/06ea6f61-ad79-4c88-921a-8aa8dc04f38b)

Reduced the image size to by 1/3 then upscaled with a scale of 3X
![X3](https://github.com/SachinSamuel01/image_upscale_python/assets/121634881/320f70a4-a3fb-4238-a71b-879a009c2295)

Reduced the image size to by 1/4 then upscaled with a scale of 4X
![X4](https://github.com/SachinSamuel01/image_upscale_python/assets/121634881/9fcb5e8b-efe6-496e-a436-47d74c1516de)

Reduced the image size to by 1/8 then upscaled with a scale of 8X
![X8](https://github.com/SachinSamuel01/image_upscale_python/assets/121634881/50dda1b2-d640-499e-b8c5-891f299c43f5)

### Performance at Different Scaling Factors
Table 1: Summary of Evaluation Metrics
<iframe src='https://sheetsu.com/tables/ae587e266c' allowfullscreen height='612' width='100%' frameBorder='0'></iframe>

Here are the plots for the PSNR, MSE, SSIM, and Time comparisons for all models at different scale values (x2, x3, x4, and x8). Each scale value is represented by a different color: red for x2, green for x3, pink for x4, and blue for x8.
![Screenshot 2024-03-09 023841](https://github.com/SachinSamuel01/image_upscale_python/assets/121634881/b0572114-82a4-4902-85bc-8fddd0873fcc)


- **Performance at Different Scaling Factors**: Each algorithm's performance varies with the scaling factor, with LAPSRN showing the best performance in terms of PSNR at scale x2.
- **Quality Comparison**: LAPSRN and ESPCN provide a good balance between quality and speed, with consistent PSNR values and low processing times across all scales.
- **Speed Analysis**: ESPCN and FSRCNN are the fastest algorithms, making them suitable for real-time upscaling tasks.

## Conclusion

The choice of the best upscaling algorithm depends on the specific requirements of the application, such as the desired balance between image quality and processing speed, and the scaling factor. ESPCN emerges as a strong contender for real-time applications requiring high-quality upscaling, while LAPSRN is suitable for scenarios demanding high-quality upscaling at lower speeds.
