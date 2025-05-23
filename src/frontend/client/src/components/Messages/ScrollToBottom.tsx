import React from 'react';

type Props = {
  scrollHandler: React.MouseEventHandler<HTMLButtonElement>;
};

export default function ScrollToBottom({ scrollHandler }: Props) {
  return (
    <div className='final-completion group mx-auto flex flex-1 gap-3 transition-all duration-300 transform-gpu md:max-w-3xl md:px-5 lg:max-w-[40rem] lg:px-1 xl:max-w-[48rem] xl:px-5 message-render focus:outline-none focus:ring-2 focus:ring-border-xheavy'>
      <button
        onClick={scrollHandler}
        className="absolute bottom-5 right-2 cursor-pointer rounded-full border border-gray-200 bg-white bg-clip-padding text-gray-600 dark:border-white/10 dark:bg-gray-850/90 dark:text-gray-200"
        aria-label="Scroll to bottom"
      >
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          className="m-1 text-black dark:text-white"
        >
          <path
            d="M17 13L12 18L7 13M12 6L12 17"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          ></path>
        </svg>
      </button>
    </div>
  );
}
