import React, { forwardRef } from "react";
// @ts-ignore
import Chat from "./Chat.svg?react";

export const ChatIcon = forwardRef<
    SVGSVGElement & { className: any },
    React.PropsWithChildren<{ className?: string }>
>(({ className, ...props }, ref) => {
    return <Chat ref={ref} {...props} className={className || ''} />;
});