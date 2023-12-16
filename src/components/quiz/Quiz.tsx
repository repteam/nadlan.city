import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "../../redux/store";
import FirstStep from "./FirstStep";
import SecondStep from "./SecondStep";
import styles from "./Quiz.module.css";
import ThirdStep from "./ThirdStep";
import FourthStep from "./FourthStep";
import FifthStep from "./FifthStep";
import SixthStep from "./SixthStep";
import Result from "./Result";
import Start from "./Start";
import End from "./End";
import Bonus from "./Bonus";
import { faClipboard } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faXmark } from "@fortawesome/free-solid-svg-icons";
import { setStep } from "../../redux/quizReducer";

const Quiz = () => {
  const step: number = useSelector((state: RootState) => state.quiz.step);

  const dispatch = useDispatch();

  return (
    <div className="h-[650px] 2xl:w-[1036px] lg:w-[780px] relative mx-auto flex flex-col items-center bg-white overflow-hidden">
      <button
        onClick={() => dispatch<any>(setStep(0))}
        className="absolute z-10 right-6 top-6"
      >
        <FontAwesomeIcon
          icon={faXmark}
          className="text-2xl hover:text-regal-red"
        />
      </button>
      <div className={styles.progressWrap}>
        <h1 className="md:text-lg sm:text-md text-sm w-5/6 flex justify-center">
          <FontAwesomeIcon
            icon={faClipboard}
            className="pr-4 text-2xl text-regal-blue"
          />
          ענו על השאלון וקבל מאיתנו מתנה
        </h1>
        {step > 0 && step < 7 && <p className={styles.steps}>{step}/6</p>}
        {step > 0 && (
          <div className={styles.progress}>
            <div
              style={{ width: `${(step - 1) * 16.7}%` }}
              className={styles.progress__inner}
            ></div>
          </div>
        )}
      </div>
      <div className="w-full h-full md:px-10 md:py-10 px-5 py-10">
        {step === 0 && <Start />}
        {step === 1 && <FirstStep />}
        {step === 2 && <SecondStep />}
        {step === 3 && <ThirdStep />}
        {step === 4 && <FourthStep />}
        {step === 5 && <FifthStep />}
        {step === 6 && <SixthStep />}
        {step === 7 && <Result />}
        {step === 8 && <Bonus />}
        {step === 9 && <End />}
      </div>
    </div>
  );
};

export default Quiz;
