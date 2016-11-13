//
//  ViewController.swift
//  Emote
//
//  Created by Robert Russo on 11/12/16.
//  Copyright © 2016 Robert Russo. All rights reserved.
//

import UIKit
import AVFoundation

class ViewController: UIViewController {
    
    let captureSession = AVCaptureSession()
    var captureDevice : AVCaptureDevice?

    override func viewDidLoad() {
        super.viewDidLoad()
        captureSession.sessionPreset = AVCaptureSessionPresetLow
        captureDevice = AVCaptureDevice.defaultDevice(withDeviceType: .builtInWideAngleCamera, mediaType: AVMediaTypeVideo, position: .back)
        
        beginSession()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    func beginSession() {
        do  {
            try captureSession.addInput(AVCaptureDeviceInput(device: captureDevice))
        } catch {
            print("ERROR!")
        }
        
        var previewLayer = AVCaptureVideoPreivewLayer(session: captureSession)
        self.view.layer.addSublayer(previewLayer)
        previewLayer?.frame = self.view.layer.fram
        captureSession.startRunning()
    }
    
    func configureDevice() {
        if let device = captureDevice {
            do {
                try device.lockForConfiguration()
            } catch {
                print("Error with device configuration")
            }
            device.focusMode = .locked
            device.unlockForConfiguration()
        }
    }

}

