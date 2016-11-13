//
//  ViewController.swift
//  Emote
//
//  Created by Robert Russo on 11/12/16.
//  Copyright © 2016 Robert Russo. All rights reserved.
//

import UIKit
import AVFoundation

class ViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    var captureSession : AVCaptureSession?
    var stillImageOutput : AVCapturePhotoOutput?
    var previewLayer : AVCaptureVideoPreviewLayer?
    
    @IBOutlet var CameraView: UIView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(<#T##animated: Bool##Bool#>)
        
        captureSession = AVCaptureSession()
        captureSession?.sessionPreset = AVCaptureSessionPresetLow

        do {
            var backCamera = AVCaptureDevice.defaultDevice(withMediaType: AVMediaTypeVideo)
            var error : NSError?
            var input = try AVCaptureDeviceInput(device: backCamera)
            
            if error == nil && captureSession!.canAddInput(input) {
                captureSession?.addInput(input)
                stillImageOutput = AVCapturePhotoOutput()
                //stillImageOutput?.= [AVVideoCodecKey : AVVideoCodecJPEG]
                stillImageOutput?. = [AVVideoCodecKey :AVVideoCodecJPEG]
            }
        } catch {
            print("Error initializing back camera")
        }
    
    }
    
}


